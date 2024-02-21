from django import template

register = template.Library()

@register.filter
def paginated_list(page_obj, max_items=5):
    num_pages = page_obj.paginator.num_pages
    current_page = page_obj.number

    # Calculate the range of page numbers to display
    display_count = 6  # Always show 6 page buttons

    # Calculate the number of pages to display before and after the current page
    half_display = display_count // 2

    if num_pages <= display_count:
        # If there are fewer pages than the display count, show all pages
        pages = list(range(1, num_pages + 1))
    elif current_page - half_display <= 1:
        # If the current page is near the beginning, display pages 1 to display_count
        pages = list(range(1, display_count + 1))
    elif current_page + half_display >= num_pages:
        # If the current page is near the end, display the last display_count pages
        pages = list(range(num_pages - display_count + 1, num_pages + 1))
    else:
        # Otherwise, center the current page and display pages accordingly
        pages = list(range(current_page - half_display, current_page + half_display + 1))

    # Add ellipses if necessary
    if pages[0] > 1:
        pages = [1, '...'] + pages
    if pages[-1] < num_pages:
        pages = pages + ['...', num_pages]

    return pages
