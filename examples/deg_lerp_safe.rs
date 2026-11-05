// stone:job stone:math.deg_lerp_safe
// stone:function deg_lerp_safe_rs

#[no_mangle]
pub extern "C" fn deg_lerp_safe_rs(a: f64, b: f64, t: f64) -> f64 {
    if !(a.is_finite() && b.is_finite() && t.is_finite()) { return f64::NAN; }
    let d = (b - a + 180.0).rem_euclid(360.0) - 180.0;
    a + d * t
}
