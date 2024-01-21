#include "head.h"
/**
 * print_python_list_info - function
 * @p: .......
 * Return: void
 **/

void print_python_list_info(PyObject *p)
  {
    long int len = PyList_Size(p);
    PyListObject *pObj = (PyListObject *)p;
    int i;

    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", pObj->allocated);

    for (i = 0; i < len; i++)
      {
	printf("Element %d: %s\n", i, Py_TYPE(pObj->ob_item[i]->tp_name));
      }
  }
