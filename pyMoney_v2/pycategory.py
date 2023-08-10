class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """initialize the different kinds of Categories"""
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    def view(self):
        """show every kinds of categories you defined before"""
        ls = []
        def view_categories(categories, space, ls):
            if space == 0:
                t = '◈'
            elif space == 3:
                t = '○'
            elif space == 6:
                t = '■'
            elif space == 9:
                t = '□'
            if(type(categories) == list):
                for i in categories:
                    view_categories(i, space+3, ls)
            else:
                ls += [" "*space + t +' '+ categories]
        view_categories(self._categories, -3, ls)
        return ls
    def is_category_valid(self, category):
        """return whether the category is in the categories you defined before """
        def inner_is_category_valid(category, categories):
            if type(categories) == list:
                for i in categories:
                    if inner_is_category_valid(category, i):
                        return True
            else:
                return category == categories
        return inner_is_category_valid(category, self._categories)
    def find_subcategories(self, category):
        """return the list of the category and its subcategories"""
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found:
                    yield categories
        k = []
        it = iter(find_subcategories_gen(category, self._categories))
        try:
            while True:
                k += [next(it)]
        except:
            return k
