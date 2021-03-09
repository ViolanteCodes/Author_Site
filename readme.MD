# A Sample Display Site for An Author, created with Django-Wagtail CMS

## Table of Contents

## Setup Order

Page Creation Order
Home Page + make available for menu
BookIndexPage as Child of HomePage + make available for menu
Series Page as Child of BookIndexPage + make available for menu
Book Page as Child of SeriesPage

Custom Settings for social media links (from admin panel)

## X.X Packages

### X.X Python-Decouple

Environmental Variable Storage
Settings for name of site and CDN links like fontawesome, bootstrap theme file, stored as environmental variables. 

### X.X Wagtail-Menus

Need to make sure pages have "add to menu enabled in sharing."

### X.X Django-Boostrap

Bootstrap theme file loads from environmental variable.

## X.X Styling

Boostrap theme link in environment

#### Maria To-Do:
- Add sample .env file
- create success url/template
- finish contact form model (header injection/ try except block)