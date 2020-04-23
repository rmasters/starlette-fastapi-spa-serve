// Application render
function render() {
    const url = new URL(window.location);
    const root = document.getElementById('main');

    switch (url.pathname) {
        case "/time":
            fetch("/data")
                .then(res => res.json())
                .then(json => root.innerText = json.time);
            break;

        case "/":
            root.innerText = "homepage";
            break;

        default:
            root.innerText = "404 Page Not Found";
            break;
    }
}

// SPA-style navigation
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', evt => {
        history.pushState({}, '', evt.target.href);
        render();
        evt.preventDefault()
    });
});

// Handle browser nav
window.addEventListener('popstate', href => {
    render();
});

render();
