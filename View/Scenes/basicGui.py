
from com.badlogic.gdx import ApplicationListener, Gdx, Input
from com.badlogic.gdx.backends.lwjgl import LwjglApplication, LwjglApplicationConfiguration
from com.badlogic.gdx.graphics import Texture, OrthographicCamera, GL10
from com.badlogic.gdx.graphics.g2d import SpriteBatch
from com.badlogic.gdx.graphics.glutils.ShapeRenderer import ShapeType
from com.badlogic.gdx.graphics.glutils import ShapeRenderer
from com.badlogic.gdx.physics.box2d import Shape

class basicGui(ApplicationListener):
    
    def __init__(self):
        self.camera = None
        self.batch = None
        self.texture = None
        self.bucketimg = None
        self.dropsound = None
        self.rainmusic = None
        self.bucket = None
        self.raindrops = None
        
        self.lastdrop = 0
        self.width = 800
        self.height = 480
        
    def create(self):    
        self.camera = OrthographicCamera()
        self.camera.setToOrtho(False, self.width, self.height)
        self.batch = SpriteBatch()
    
    

    def render(self):
        Gdx.gl.glClearColor(0,0,0.2,0)
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT)
        self.batch.begin()
        self.camera.update()
        shapeRenderer = ShapeRenderer()
        shapes = ShapeType.Filled
        shapeRenderer.begin(shapes);
        shapeRenderer.setColor(0, 1, 0, 1);
        shapeRenderer.rect(0, 0, 100, 100);
        shapeRenderer.end();
        self.batch.end()
        
    def resize(self,x,y):
        pass
    
    def dispose(self):
        self.batch.dispose()