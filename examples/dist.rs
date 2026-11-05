// stone:job stone:math.dist
// stone:function dist_rs

#[no_mangle]
pub extern "C" fn dist_rs(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    (x2 - x1).hypot(y2 - y1)
}
