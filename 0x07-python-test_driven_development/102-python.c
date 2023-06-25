#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t size;
    const char *str;
    PyUnicodeObject *unicode;

    if (!PyUnicode_Check(p)) {
        printf("Error: Invalid string object\n");
        return;
    }

    size = PyUnicode_GET_SIZE(p);
    str = PyUnicode_AsUTF8(p);

    printf("  %s", str);
    printf("  (size=%ld)\n", size);

    unicode = (PyUnicodeObject *) p;
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(unicode) ? "compact ascii" : "unicode");
}
