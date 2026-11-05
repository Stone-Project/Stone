// stone:job stone:math.inverse_lerp
// stone:function inverse_lerp_rs

#[no_mangle]
pub extern "C" fn inverse_lerp_rs(a: f64, b: f64, x: f64) -> f64 {
    (x - a) / (b - a)
}
