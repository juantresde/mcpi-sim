'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_INTEL_parallel_arrays'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_INTEL_parallel_arrays',False)
_p.unpack_constants( """GL_PARALLEL_ARRAYS_INTEL 0x83F4
GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL 0x83F5
GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL 0x83F6
GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL 0x83F7
GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL 0x83F8""", globals())
glget.addGLGetConstant( GL_PARALLEL_ARRAYS_INTEL, (1,) )
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,arrays.GLvoidpArray)
def glVertexPointervINTEL( size,type,pointer ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glNormalPointervINTEL( type,pointer ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,arrays.GLvoidpArray)
def glColorPointervINTEL( size,type,pointer ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,arrays.GLvoidpArray)
def glTexCoordPointervINTEL( size,type,pointer ):pass


def glInitParallelArraysINTEL():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
