from functools import wraps
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

monokai_theme = Theme({
    "header": "bold magenta",
})

console = Console(theme=monokai_theme)


def log_headers(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        table = Table(
            title=":sparkles::soft_ice_cream:Request Headers:shaved_ice::ice_cream:")

        table.add_column("Key", style="bold magenta")
        table.add_column("Value", style="green")

        for key, value in dict(request.headers).items():
            table.add_row(str(key), str(value))

        console.print(table)

        return view_func(request, *args, **kwargs)

    return wrapper
