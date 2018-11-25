from pathlib import Path

from .api_doc import ApiDoc
from .helpers import (
    ExampleContainer,
    HighlightedSource,
    load_source_with_environment,
)
from .metadata import get_component_metadata

HERE = Path(__file__).parent

fade_source = (HERE / "components" / "fade.py").read_text()


def get_content(app):
    return [
        ExampleContainer(
            load_source_with_environment(fade_source, "fade", {"app": app})
        ),
        HighlightedSource(fade_source),
        ApiDoc(get_component_metadata("src/components/Fade.js")),
    ]
