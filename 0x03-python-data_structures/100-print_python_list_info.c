#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - shows info about Python lists
 * @p: object
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, b, j;

	j = 0;
	PyObject *obj;

	list_size = PyList_Size(p);
	b = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", b);
	while (j < list_size)
	{
		obj = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, Py_TYPE(obj)->tp_name);
		j++;
	}
}
