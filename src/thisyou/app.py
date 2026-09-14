"""FastAPI application for the first thisyou web slice."""

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .profile_service import (
    Profile,
    ProfileLookupError,
    get_profile,
    normalize_handle,
)

app = FastAPI(title="thisyou.dev", version="0.1.0")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/health", include_in_schema=False)
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"profile": None, "error": None},
    )


@app.post("/profile", response_class=HTMLResponse)
def profile(request: Request, handle: str = Form(...)) -> HTMLResponse:
    normalized_handle = normalize_handle(handle)
    profile: Profile | None = None
    error: str | None = None

    if not normalized_handle:
        error = "Give us a valid Bluesky handle first."
    else:
        try:
            profile = get_profile(normalized_handle)
        except ProfileLookupError as lookup_error:
            error = str(lookup_error)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"profile": profile, "error": error},
    )
