from ctypes import (
    pointer,
    POINTER,
    Structure,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_short,
    c_ubyte,
    c_float,
    c_ushort,
    c_void_p,
    c_int,
    c_uint,
    c_long,
    c_ulong,
    c_longlong,
    c_ulonglong,
    c_longdouble
)

Bool = c_bool  # C type: _Bool  Python type: bool (1)
Char = c_char  # C type: char  Python type: 1-character bytes object
UChar = c_ubyte  # C type: unsigned char  Python type: int
Short = c_short  # C type: short  Python type: int
UShort = c_ushort  # C type: unsigned short  Python type: int
Int = c_int  # C type: int  Python type: int
UInt = c_uint  # C type: unsigned int  Python type: int
Long = c_long  # C type: long  Python type: int
ULong = c_ulong  # C type: unsigned long  Python type: int
ULLong = c_longlong  # C type: __int64 or long-long  Python type: int
ULLong = c_ulonglong  # C type: unsigned __int64 or unsigned long-long  Python type: int
Float = c_float  # C type: float  Python type: float
Double = c_double  # C type: double  Python type: float
LDouble = c_longdouble  # C type: long double  Python type: float
CharPnt = c_char_p  # C type: char* (NUL terminated)  Python type: bytes object or None
VoidPtr = c_void_p  # C type: wchar_t* (NUL terminated)  Python type: int or None
Void = c_void_p  # C type: void  Python type: None


def _to_int(value: float):
    return int(value) if isinstance(value, float) else value


def _to_float(value: int):
    return float(value) if isinstance(value, int) else value


def _to_byte_str(value: str):
    if not isinstance(value, (str, bytes)):
        value = str(value)
    return value.encode('utf-8', 'ignore')


def _to_str(value: bytes):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def copyDataTo(src, dest):
    pointer(dest)[0] = pointer(src)[0]


# ----------------------------------------------------------------------------------
# Structures Definition
# ----------------------------------------------------------------------------------

# Vector2, 2 components
class Vector2(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
    ]

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i


# Vector3, 3 components
class Vector3(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
    ]

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = i


# Vector4, 4 components
class Vector4(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
        ('w', Float),  # Vector w component
    ]

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = i

    @property
    def w(self) -> float:
        return self.w.value

    @w.setter
    def w(self, i: float) -> None:
        self.w = i


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4


# Matrix, 4x4 components, column major, OpenGL style, right-handed
class Matrix(Structure):
    _fields_ = [
        ('m0', Float), ('m4', Float), ('m8', Float), ('m12', Float),  # Matrix first row (4 components)
        ('m1', Float), ('m5', Float), ('m9', Float), ('m13', Float),  # Matrix second row (4 components)
        ('m2', Float), ('m6', Float), ('m10', Float), ('m14', Float),  # Matrix third row (4 components)
        ('m3', Float), ('m7', Float), ('m11', Float), ('m15', Float),  # Matrix fourth row (4 components)
    ]

    @property
    def m0(self) -> float:
        return self.m0.value

    @m0.setter
    def m0(self, i: float) -> None:
        self.m0 = i

    @property
    def m1(self) -> float:
        return self.m1.value

    @m1.setter
    def m1(self, i: float) -> None:
        self.m1 = i

    @property
    def m2(self) -> float:
        return self.m2.value

    @m2.setter
    def m2(self, i: float) -> None:
        self.m2 = i

    @property
    def m3(self) -> float:
        return self.m3.value

    @m3.setter
    def m3(self, i: float) -> None:
        self.m3 = i

    @property
    def m4(self) -> float:
        return self.m4.value

    @m4.setter
    def m4(self, i: float) -> None:
        self.m4 = i

    @property
    def m5(self) -> float:
        return self.m5.value

    @m5.setter
    def m5(self, i: float) -> None:
        self.m5 = i

    @property
    def m6(self) -> float:
        return self.m6.value

    @m6.setter
    def m6(self, i: float) -> None:
        self.m6 = i

    @property
    def m7(self) -> float:
        return self.m7.value

    @m7.setter
    def m7(self, i: float) -> None:
        self.m7 = i

    @property
    def m8(self) -> float:
        return self.m8.value

    @m8.setter
    def m8(self, i: float) -> None:
        self.m8 = i

    @property
    def m9(self) -> float:
        return self.m9.value

    @m9.setter
    def m9(self, i: float) -> None:
        self.m9 = i

    @property
    def m10(self) -> float:
        return self.m10.value

    @m10.setter
    def m10(self, i: float) -> None:
        self.m10 = i

    @property
    def m11(self) -> float:
        return self.m11.value

    @m11.setter
    def m11(self, i: float) -> None:
        self.m11 = i

    @property
    def m12(self) -> float:
        return self.m12.value

    @m12.setter
    def m12(self, i: float) -> None:
        self.m12 = i

    @property
    def m13(self) -> float:
        return self.m13.value

    @m13.setter
    def m13(self, i: float) -> None:
        self.m13 = i

    @property
    def m14(self) -> float:
        return self.m14.value

    @m14.setter
    def m14(self, i: float) -> None:
        self.m14 = i

    @property
    def m15(self) -> float:
        return self.m15.value

    @m15.setter
    def m15(self, i: float) -> None:
        self.m15 = i


# Color, 4 components, R8G8B8A8 (32bit)
class Color(Structure):
    _fields_ = [
        ('r', UChar),  # Color red value
        ('g', UChar),  # Color green value
        ('b', UChar),  # Color blue value
        ('a', UChar),  # Color alpha value
    ]

    @property
    def r(self) -> int:
        return self.r.value

    @r.setter
    def r(self, i: int) -> None:
        self.r = i

    @property
    def g(self) -> int:
        return self.g.value

    @g.setter
    def g(self, i: int) -> None:
        self.g = i

    @property
    def b(self) -> int:
        return self.b.value

    @b.setter
    def b(self, i: int) -> None:
        self.b = i

    @property
    def a(self) -> int:
        return self.a.value

    @a.setter
    def a(self, i: int) -> None:
        self.a = i


# Rectangle, 4 components
class Rectangle(Structure):
    _fields_ = [
        ('x', Float),  # Color red value
        ('y', Float),  # Color green value
        ('width', Float),  # Color blue value
        ('height', Float),  # Color alpha value
    ]

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    @property
    def width(self) -> float:
        return self.width.value

    @width.setter
    def width(self, i: float) -> None:
        self.width = i

    @property
    def height(self) -> float:
        return self.height.value

    @height.setter
    def height(self, i: float) -> None:
        self.height = i


# Image, pixel data stored in CPU memory (RAM)
class Image(Structure):
    _fields_ = [
        ('data', VoidPtr),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    @property
    def data(self) -> VoidPtr:
        return self.data.value

    @data.setter
    def data(self, i: VoidPtr) -> None:
        self.data = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = i

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = i


# Texture, tex data stored in GPU memory (VRAM)
class Texture(Structure):
    _fields_ = [
        ('id', UInt),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    @property
    def id(self) -> UInt:
        return self.id.value

    @id.setter
    def id(self, i: UInt) -> None:
        self.id = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = i

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = i


# Texture2D, same as Texture
Texture2D = Texture

# TextureCubemap, same as Texture
TextureCubemap = Texture


# RenderTexture, fbo for texture rendering
class RenderTexture(Structure):
    _fields_ = [
        ('id', UInt),  # OpenGL framebuffer object id
        ('texture', Texture),  # Image base width
        ('depth', Texture)  # Image base width
    ]

    @property
    def id(self) -> int:
        return self.id.value

    @id.setter
    def id(self, i: int) -> None:
        self.id = i

    @property
    def texture(self) -> Texture:
        return self.texture

    @texture.setter
    def texture(self, i: Texture) -> None:
        self.texture = i

    @property
    def depth(self) -> Texture:
        return self.depth

    @depth.setter
    def depth(self, i: Texture) -> None:
        self.depth = i


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture


# NPatchInfo, n-patch layout infoStructureers
class NPatchInfo(Structure):
    _fields_ = [
        ('source', Rectangle),  # Texture source rectangle
        ('left', Int),  # Left border offset
        ('top', Int),  # Top border offset
        ('right', Int),  # Right border offset
        ('bottom', Int),  # Bottom border offset
        ('layout', Int)  # Layout of the n-patch: 3x3, 1x3 or 3x1
    ]

    @property
    def source(self) -> Rectangle:
        return self.source.value

    @source.setter
    def source(self, i: Rectangle) -> None:
        self.source = i

    @property
    def left(self) -> int:
        return self.left.value

    @left.setter
    def left(self, i: int) -> None:
        self.left = i

    @property
    def top(self) -> int:
        return self.top.value

    @top.setter
    def top(self, i: int) -> None:
        self.top = i

    @property
    def right(self) -> int:
        return self.right.value

    @right.setter
    def right(self, i: int) -> None:
        self.right = i

    @property
    def bottom(self) -> int:
        return self.bottom.value

    @bottom.setter
    def bottom(self, i: int) -> None:
        self.bottom = i

    @property
    def layout(self) -> int:
        return self.layout.value

    @layout.setter
    def layout(self, i: int) -> None:
        self.layout = i


# GlyphInfo, font characters glyphs info
class GlyphInfo(Structure):
    _fields_ = [
        ('value', Int),  # Character value (Unicode)
        ('offsetX', Int),  # Character offset X when drawing
        ('offsetY', Int),  # Character offset Y when drawing
        ('advanceX', Int),  # Character advance position X
        ('image', Image)  # Character image data
    ]

    @property
    def value(self) -> int:
        return self.value.value

    @value.setter
    def value(self, i: int) -> None:
        self.value = i

    @property
    def offsetX(self) -> int:
        return self.offsetX.value

    @offsetX.setter
    def offsetX(self, i: int) -> None:
        self.offsetX = i

    @property
    def offsetY(self) -> int:
        return self.offsetY.value

    @offsetY.setter
    def offsetY(self, i: int) -> None:
        self.offsetY = i

    @property
    def advanceX(self) -> int:
        return self.advanceX.value

    @advanceX.setter
    def advanceX(self, i: int) -> None:
        self.advanceX = i

    @property
    def image(self) -> Image:
        return self.image.value

    @image.setter
    def image(self, i: Image) -> None:
        self.image = i


# Font, font texture and GlyphInfo array data
class Font(Structure):
    _fields_ = [
        ('baseSize', Int),  # Character value (Unicode)
        ('glyphCount', Int),  # Character offset X when drawing
        ('glyphPadding', Int),  # Character offset Y when drawing
        ('texture', Texture2D),  # Character advance position X
        ('recs', POINTER(Rectangle)),  # Character image data
        ('glyphs', POINTER(GlyphInfo))  # Character image data
    ]

    @property
    def baseSize(self) -> int:
        return self.baseSize.value

    @baseSize.setter
    def baseSize(self, i: int) -> None:
        self.baseSize = i

    @property
    def glyphCount(self) -> int:
        return self.glyphCount.value

    @glyphCount.setter
    def glyphCount(self, i: int) -> None:
        self.glyphCount = i

    @property
    def glyphPadding(self) -> int:
        return self.glyphPadding.value

    @glyphPadding.setter
    def glyphPadding(self, i: int) -> None:
        self.glyphPadding = i

    @property
    def texture(self) -> Texture2D:
        return self.texture.value

    @texture.setter
    def texture(self, i: Texture2D) -> None:
        self.texture = i

    @property
    def recs(self) -> POINTER(Rectangle):
        return self.recs

    @recs.setter
    def recs(self, i: POINTER(Rectangle)) -> None:
        self.recs = i

    @property
    def glyphs(self) -> POINTER(GlyphInfo):
        return self.glyphs

    @glyphs.setter
    def glyphs(self, i: POINTER(GlyphInfo)) -> None:
        self.glyphs = i
