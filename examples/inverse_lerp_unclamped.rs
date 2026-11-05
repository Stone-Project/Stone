// stone:job stone:math.inverse_lerp_unclamped
// stone:function inverse_lerp_unclamped_rs

#[no_mangle]
pub extern "C" fn inverse_lerp_unclamped_rs(a: f64, b: f64, x: f64) -> f64 {
    if a == b { return f64::NAN; }
    (x - a) / (b - a)
}
