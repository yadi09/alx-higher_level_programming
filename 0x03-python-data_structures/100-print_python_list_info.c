
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function
 * @p: .......
 * Return: void
 **/

void print_python_list_info(PyObject *p)
  {
    Py_ssize_t len = PyList_Size(p);
    PyListObject *pObj = (PyListObject *)p;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < len; i++)
      {
	printf("Element %ld: %s\n", i, Py_TYPE(pObj->ob_item[i]->tp_name));
      }
  }
