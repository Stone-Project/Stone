// stone:job stone:math.lerp_safe
// stone:function lerp_safe_rs

#[no_mangle]
pub extern "C" fn lerp_safe_rs(start: f64, end: f64, t: f64) -> f64 {
    if !(start.is_finite() && end.is_finite() && t.is_finite()) { return f64::NAN; }
    start + (end - start) * t
}
