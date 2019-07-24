#include <Python.h>
#include "perlin.h"


static PyObject* perlin_noise(PyObject* self, PyObject *args)
{
    double x, y, z, w;
    if(PyArg_ParseTuple(args, "dddd", &x, &y, &z, &w)){
        return Py_BuildValue("d", (double)noise(x, y, z, w));
    }
    return NULL;
}


static PyMethodDef perlin_methods[] = {
    {"noise", (PyCFunction)perlin_noise, METH_VARARGS,
    "Takes 4 floats as coordinates, returns a 4D Perlin noise value for that point."},
    {NULL, NULL}
};


static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "perlin",
        NULL,
        -1,
        perlin_methods,
        NULL,
        NULL,
        NULL,
        NULL
};


PyMODINIT_FUNC PyInit_perlin(void)
{
    PyObject *perlinmodule = PyModule_Create(&moduledef);

    if (perlinmodule == NULL)
        return NULL; // INITERROR
    return perlinmodule;
}