// stone:job stone:math.inverse_lerp_safe
// stone:function inverse_lerp_safe_rs

#[no_mangle]
pub extern "C" fn inverse_lerp_safe_rs(a: f64, b: f64, x: f64) -> f64 {
    if !(a.is_finite() && b.is_finite() && x.is_finite()) { return f64::NAN; }
    if a == b { return f64::NAN; }
    (x - a) / (b - a)
}
