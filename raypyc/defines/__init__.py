RLGL_VERSION: str = 4.2
RL_DEFAULT_BATCH_BUFFER_ELEMENTS: int = 8192
RL_DEFAULT_BATCH_BUFFERS: int = 1  # Default number of batch buffers (multi-buffering)
RL_DEFAULT_BATCH_DRAWCALLS: int = 256  # Default number of batch draw calls (by state changes: mode, texture)
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS: int = 4  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
RL_MAX_MATRIX_STACK_SIZE: int = 32  # Maximum size of Matrix stack
RL_MAX_SHADER_LOCATIONS: int = 32  # Maximum number of shader locations supported
RL_TEXTURE_WRAP_S: int = 10242  # GL_TEXTURE_WRAP_S
RL_TEXTURE_WRAP_T: int = 10243  # GL_TEXTURE_WRAP_T
RL_TEXTURE_MAG_FILTER: int = 10240  # GL_TEXTURE_MAG_FILTER
RL_TEXTURE_MIN_FILTER: int = 10241  # GL_TEXTURE_MIN_FILTER
RL_TEXTURE_FILTER_NEAREST: int = 9728  # GL_NEAREST
RL_TEXTURE_FILTER_LINEAR: int = 9729  # GL_LINEAR
RL_TEXTURE_FILTER_MIP_NEAREST: int = 9984  # GL_NEAREST_MIPMAP_NEAREST
RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR: int = 9986  # GL_NEAREST_MIPMAP_LINEAR
RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST: int = 9985  # GL_LINEAR_MIPMAP_NEAREST
RL_TEXTURE_FILTER_MIP_LINEAR: int = 9987  # GL_LINEAR_MIPMAP_LINEAR
RL_TEXTURE_FILTER_ANISOTROPIC: int = 12288  # Anisotropic filter (custom identifier)
RL_TEXTURE_MIPMAP_BIAS_RATIO: int = 16384  # Texture mipmap bias, percentage ratio (custom identifier)
RL_TEXTURE_WRAP_REPEAT: int = 10497  # GL_REPEAT
RL_TEXTURE_WRAP_CLAMP: int = 33071  # GL_CLAMP_TO_EDGE
RL_TEXTURE_WRAP_MIRROR_REPEAT: int = 33648  # GL_MIRRORED_REPEAT
RL_TEXTURE_WRAP_MIRROR_CLAMP: int = 34626  # GL_MIRROR_CLAMP_EXT
RL_MODELVIEW: int = 5888  # GL_MODELVIEW
RL_PROJECTION: int = 5889  # GL_PROJECTION
RL_TEXTURE: int = 5890  # GL_TEXTURE
RL_LINES: int = 1  # GL_LINES
RL_TRIANGLES: int = 4  # GL_TRIANGLES
RL_QUADS: int = 7  # GL_QUADS
RL_UNSIGNED_BYTE: int = 5121  # GL_UNSIGNED_BYTE
RL_FLOAT: int = 5126  # GL_FLOAT
RL_STREAM_DRAW: int = 35040  # GL_STREAM_DRAW
RL_STREAM_READ: int = 35041  # GL_STREAM_READ
RL_STREAM_COPY: int = 35042  # GL_STREAM_COPY
RL_STATIC_DRAW: int = 35044  # GL_STATIC_DRAW
RL_STATIC_READ: int = 35045  # GL_STATIC_READ
RL_STATIC_COPY: int = 35046  # GL_STATIC_COPY
RL_DYNAMIC_DRAW: int = 35048  # GL_DYNAMIC_DRAW
RL_DYNAMIC_READ: int = 35049  # GL_DYNAMIC_READ
RL_DYNAMIC_COPY: int = 35050  # GL_DYNAMIC_COPY
RL_FRAGMENT_SHADER: int = 35632  # GL_FRAGMENT_SHADER
RL_VERTEX_SHADER: int = 35633  # GL_VERTEX_SHADER
RL_COMPUTE_SHADER: int = 37305  # GL_COMPUTE_SHADER
PI: int = 3.141592653589793
DEG2RAD: float = (PI/180.0)
RAD2DEG: float = (180.0/PI)
GL_SHADING_LANGUAGE_VERSION: int = 35724
GL_COMPRESSED_RGB_S3TC_DXT1_EXT: int = 33776
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT: int = 33777
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT: int = 33778
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT: int = 33779
GL_ETC1_RGB8_OES: int = 36196
GL_COMPRESSED_RGB8_ETC2: int = 37492
GL_COMPRESSED_RGBA8_ETC2_EAC: int = 37496
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG: int = 35840
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG: int = 35842
GL_COMPRESSED_RGBA_ASTC_4x4_KHR: int = 37808
GL_COMPRESSED_RGBA_ASTC_8x8_KHR: int = 37815
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: int = 34047
GL_TEXTURE_MAX_ANISOTROPY_EXT: int = 34046
GL_UNSIGNED_SHORT_5_6_5: int = 33635
GL_UNSIGNED_SHORT_5_5_5_1: int = 32820
GL_UNSIGNED_SHORT_4_4_4_4: int = 32819
GL_LUMINANCE: int = 6409
GL_LUMINANCE_ALPHA: int = 6410
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str = vertexPosition  # Binded by default to shader location: 0
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str = vertexTexCoord  # Binded by default to shader location: 1
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str = vertexNormal  # Binded by default to shader location: 2
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str = vertexColor  # Binded by default to shader location: 3
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str = vertexTangent  # Binded by default to shader location: 4
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str = vertexTexCoord2  # Binded by default to shader location: 5
RL_DEFAULT_SHADER_UNIFORM_NAME_MVP: str = mvp  # model-view-projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW: str = matView  # view matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION: str = matProjection  # projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL: str = matModel  # model matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL: str = matNormal  # normal matrix (transpose(inverse(matModelView))
RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR: str = colDiffuse  # color diffuse (base tint color, multiplied by texture color)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0: str = texture0  # texture0 (texture slot active 0)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1: str = texture1  # texture1 (texture slot active 1)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2: str = texture2  # texture2 (texture slot active 2)
RAYLIB_VERSION: str = 4.2
EPSILON: int = 1e-06
RAYGUI_VERSION: str = 3.2
SCROLLBAR_LEFT_SIDE: int = 0
SCROLLBAR_RIGHT_SIDE: int = 1
RAYGUI_ICON_SIZE: int = 16  # Size of icons in pixels (squared)
RAYGUI_ICON_MAX_ICONS: int = 256  # Maximum number of icons
RAYGUI_ICON_MAX_NAME_LENGTH: int = 32  # Maximum length of icon name id
RAYGUI_MAX_CONTROLS: int = 16  # Maximum number of standard controls
RAYGUI_MAX_PROPS_BASE: int = 16  # Maximum number of standard properties
RAYGUI_MAX_PROPS_EXTENDED: int = 8  # Maximum number of extended properties
KEY_RIGHT: int = 262
KEY_LEFT: int = 263
KEY_DOWN: int = 264
KEY_UP: int = 265
KEY_BACKSPACE: int = 259
KEY_ENTER: int = 257
RAYGUI_WINDOWBOX_STATUSBAR_HEIGHT: int = 24
RAYGUI_GROUPBOX_LINE_THICK: int = 1
RAYGUI_LINE_MARGIN_TEXT: int = 12
RAYGUI_LINE_TEXT_PADDING: int = 4
RAYGUI_PANEL_BORDER_WIDTH: int = 1
RAYGUI_TOGGLEGROUP_MAX_ITEMS: int = 32
RAYGUI_VALUEBOX_MAX_CHARS: int = 32
RAYGUI_COLORBARALPHA_CHECKED_SIZE: int = 10
RAYGUI_MESSAGEBOX_BUTTON_HEIGHT: int = 24
RAYGUI_MESSAGEBOX_BUTTON_PADDING: int = 12
RAYGUI_TEXTINPUTBOX_BUTTON_HEIGHT: int = 28
RAYGUI_TEXTINPUTBOX_BUTTON_PADDING: int = 12
RAYGUI_TEXTINPUTBOX_HEIGHT: int = 28
RAYGUI_GRID_ALPHA: int = 0.15
MAX_LINE_BUFFER_SIZE: int = 256
ICON_TEXT_PADDING: int = 4
RAYGUI_TEXTSPLIT_MAX_ITEMS: int = 128
RAYGUI_TEXTSPLIT_MAX_TEXT_SIZE: int = 1024
RAYGUI_TEXTFORMAT_MAX_SIZE: int = 256
