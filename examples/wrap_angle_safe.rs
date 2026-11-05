// stone:job stone:math.wrap_angle_safe
// stone:function wrap_angle_safe_rs

#[no_mangle]
pub extern "C" fn wrap_angle_safe_rs(a: f64) -> f64 {
    if !a.is_finite() { return f64::NAN; }
    const PI: f64 = std::f64::consts::PI;
    (a + PI).rem_euclid(2.0 * PI) - PI
}
