from shiny import App, render, ui, reactive
from Bio.Seq import Seq

app_ui = ui.page_fluid(
    ui.include_css("www/styles.css"),
    ui.div(
        ui.h2("DNA/RNA to Protein Translator"),
        ui.div(
            ui.div(
                ui.p("Paste your DNA or RNA sequence below:"),
                ui.input_text_area(
                    "sequence",
                    label="",
                    placeholder="Enter DNA or RNA sequence here",
                    rows=6,
                ),
                class_="input-section",
            ),
            ui.div("\u2192", class_="arrow"),
            ui.div(
                ui.h4("Translated Protein:"),
                ui.output_text_verbatim("protein_output"),
                class_="output-section",
            ),
            class_="translator-container",
        ),
        class_="translator-card",
    ),
    ui.tags.footer(
        ui.p(
            "Powered by Biopython & Shiny for Python",
            style="text-align: center; padding-top: 20px;",
        )
    ),
)


def server(input, output, session):
    @reactive.Calc
    def cleaned_seq():
        seq = input.sequence().strip().upper()
        return seq.replace(" ", "").replace("\n", "")

    @output
    @render.text
    def protein_output():
        seq_str = cleaned_seq()
        if not seq_str:
            return "Please enter a sequence."
        try:
            # Convert RNA to DNA if needed
            dna_seq = seq_str.replace("U", "T")
            # Use Biopython to perform translation
            protein = Seq(dna_seq).translate(to_stop=False)
            return str(protein)
        except Exception as e:
            return f"Error translating sequence: {e}"


app = App(app_ui, server)
