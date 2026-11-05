// stone:job stone:math.mul
// stone:function mul_rs

#[no_mangle]
pub extern "C" fn mul_rs(x: f64, y: f64) -> f64 {
    x * y
}
