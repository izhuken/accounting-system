from typing import Callable

from flet import Container, Page, RouteChangeEvent, TemplateRoute


class Router:
    def __init__(self):
        self.routes: dict[str, Callable] = {}
        self.body = Container(expand=True)
        self.page: Page | None = None

    def set_routes(self, route_dictionary: dict) -> None:
        self.routes.update(route_dictionary)

    async def route_change(self, route: RouteChangeEvent) -> None:
        for collected_route in self.routes.keys():
            redirect_route = route.route
            template_route = TemplateRoute(redirect_route)

            if template_route.match(collected_route):
                route_params = template_route.__dict__.get(
                    "_TemplateRoute__last_params"
                )
                self.body.content = self.routes[collected_route](self, **route_params)
                self.body.update()

    def is_current_page(self, route, exact: bool = False):
        if exact:
            return route == self.page.route

        return self.page.route.startswith(route)

    def go(self, route: str) -> None:
        if not self.page:
            raise Exception("Page not set")

        self.page.go(route)
