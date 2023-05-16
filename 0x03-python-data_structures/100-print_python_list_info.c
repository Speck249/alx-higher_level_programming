#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
*print_python_list_info - prints basic info about python list
*@ptr: parameter
*Return: no return value
**/

void print_python_list_info(PyObject *ptr)
{
long int size = PyList_Size(ptr);
int n;
PyListObject *obj = (PyListObject *)ptr;

printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj->allocated);
for (n = 0; n < size; n++)
printf("Element %d: %s\n", n, Py_TYPE(obj->ob_item[n])->tp_name);
}
