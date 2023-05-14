# encyclopedia-django

## Description

This repository contains a Django web application that implements a Wiki encyclopedia. The project utilizes Markdown, a lightweight markup language, to store and format encyclopedia entries. Users can create, edit, and view encyclopedia entries, with Markdown content automatically converted to HTML for display.

## Key Features

- **Entry Page**: Each encyclopedia entry has its own dedicated page, displaying the contents of the entry. If an entry does not exist, a user-friendly error page is shown.
- **Index Page**: The index page lists all the encyclopedia entries, allowing users to click on any entry name to directly access that entry's page.
- **Search**: Users can search for specific entries by typing queries into the search box. The search functionality provides relevant search results, redirecting users to the requested entry or displaying a list of matching entries.
- **New Page**: Users can create new encyclopedia entries by providing a title and Markdown content through a user-friendly interface. Duplicate title submissions are handled, and saved entries are accessible through their respective pages.
- **Edit Page**: Each entry page includes an option to edit the entry's Markdown content. The content is pre-populated in a textarea, and users can save their changes, with redirection back to the edited entry's page.
- **Random Page**: Users can navigate to a random encyclopedia entry by clicking the "Random Page" option in the sidebar.
- **Markdown to HTML Conversion**: The Markdown content of each entry is converted to HTML for proper rendering on the entry's page. The conversion is performed using the python-markdown2 package.

This repository provides a complete implementation of the Wiki encyclopedia project, offering an intuitive and interactive platform for managing and accessing knowledge through a Markdown-based encyclopedia.
