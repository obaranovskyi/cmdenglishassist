from .consts import ROWS, COLUMNS
from .core import add_next_line_on_long_phrase
from .pdf_grid import print_pdf_grid


class CardGenerator:

    def convert(self, words):
        pages = self.words_to_page(words)
        table = self.pages_to_table(pages)
        original_pages = []
        translation_pages = []
        for page in table:
            for row in page:
                original_row = []
                translation_row = []
                for word in row:
                    new_original_value = add_next_line_on_long_phrase(word['original_value'])
                    original_row.append(new_original_value)
                    new_translation_value = add_next_line_on_long_phrase(word['translation'])
                    translation_row.insert(0, new_translation_value)
                original_pages.append(original_row)
                translation_pages.append(translation_row)
        ready_to_print_table = [*original_pages, *translation_pages]
        print_pdf_grid(ready_to_print_table)

    def words_to_page(self, words):
        page_words_count = ROWS * COLUMNS
        pages = []
        page_words = []
        for index, word in enumerate(words):
            is_last = index == len(words) - 1
            page_words.append(word) 
            if len(page_words) == page_words_count:
                pages.append(page_words)
                page_words = []
            # Fill empty cells with empty objects
            if is_last and len(page_words) > 0:
                empty_word = { 'original_value': '', 'translation': '' }
                for i in range(0, page_words_count - len(page_words)):
                    page_words.append(empty_word)
                pages.append(page_words)
                page_words = []
        return pages

    def pages_to_table(self, pages):
        row = []
        page = []
        table = []
        for word_page in pages:
            for word in word_page:
                row.append(word)
                if len(row) == COLUMNS:
                    page.append(row)
                    row = []
                if len(page) == ROWS:
                    table.append(page)
                    page = []
        return table

