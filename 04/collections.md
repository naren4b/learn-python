| Data Type | Description | Syntax (Delimiter) | Example |
|-----------|-------------|-------------------|---------|
| List | Ordered, changeable, allows duplicate members | Square brackets `[]` | `['apple', 'banana', 'cherry', 'apple']` |
| Tuple | Ordered, unchangeable (immutable), allows duplicate members | Parentheses `()` | `('carrot', 'potato', 'onion')` |
| Set | Unordered, changeable, but no duplicate members | Curly braces `{}` or `set()` function | `{'red', 'green', 'blue'}` |
| Dictionary | Ordered (since Python 3.7), changeable collection of key:value pairs | Curly braces `{}` with colons `:` | `{'name': 'Alice', 'age': 30, 'city': 'New York'}` |


# Key Differences Between Lists and Sets

The main differences between Python lists and sets are that lists are ordered and allow duplicate elements, while sets are unordered and contain only unique elements.

| Feature | List | Set |
|---------|------|-----|
| Order | Ordered (maintains insertion order) | Unordered (elements have no specific position) |
| Duplicates | Allows duplicate elements | Does not allow duplicates; only unique elements |
| Indexing | Supports indexing and slicing (e.g., `my_list[0]`) | Does not support indexing or slicing |
| Syntax | Defined using square brackets `[]` | Defined using curly braces `{}` or `set()` |
| Mutability | Mutable (elements can be added, removed, or changed) | Mutable (elements can be added or removed, but not changed by index) |
| Element Types | Can contain any object, including lists or dictionaries | Can only contain hashable (immutable) objects like numbers, strings, or tuples |
| Performance | Slower for membership tests `(x in my_list)` - O(n) complexity | Significantly faster for membership tests - O(1) average complexity due to hash table implementation |