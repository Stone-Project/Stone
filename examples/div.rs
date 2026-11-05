// stone:job stone:math.div
// stone:function div_rs

#[no_mangle]
pub extern "C" fn div_rs(x: f64, y: f64) -> f64 {
    x / y
}
