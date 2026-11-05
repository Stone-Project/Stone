// stone:job stone:math.wrap_degrees_safe
// stone:function wrap_degrees_safe_rs

#[no_mangle]
pub extern "C" fn wrap_degrees_safe_rs(d: f64) -> f64 {
    if !d.is_finite() { return f64::NAN; }
    (d + 180.0).rem_euclid(360.0) - 180.0
}
