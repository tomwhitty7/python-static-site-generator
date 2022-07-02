import typer as typer
import site from ssg

def main(source, dest):
    source="content"
    dest="dist"

    config = {source="source", dest="dest"}
    Site(**config)

typer.run(main())
