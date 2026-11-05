// stone:job stone:math.hypot3_safe
// stone:function hypot3_safe_rs

#[no_mangle]
pub extern "C" fn hypot3_safe_rs(a: f64, b: f64, c: f64) -> f64 {
    if !(a.is_finite() && b.is_finite() && c.is_finite()) { return f64::NAN; }
    (a * a + b * b + c * c).sqrt()
}
