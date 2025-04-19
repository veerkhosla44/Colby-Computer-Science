trait Drawable {
    fn draw(&self);
}

struct Circle {
    radius: f32,
}

struct Rectangle {
    width: f32,
    height: f32,
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle with radius: {}", self.radius);
    }
}

impl Drawable for Rectangle {
    fn draw(&self) {
        println!("Drawing a rectangle with width: {} and height: {}", self.width, self.height);
    }
}
