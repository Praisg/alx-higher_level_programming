#include <Python.h>

/**
 * print_python_list_info -  about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int si_ze, alloc, i;
	PyObject *obj;

	si_ze = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", si_ze);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < si_ze; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

