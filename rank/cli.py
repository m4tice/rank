import click
import rank.helper as h


@click.command()
@click.option('--input_file', '-i', help="input file that contains matches information", required=True)
def cli(input_file):
    h.generate(input_file)


