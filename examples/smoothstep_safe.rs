// stone:job stone:math.smoothstep_safe
// stone:function smoothstep_safe_rs

#[no_mangle]
pub extern "C" fn smoothstep_safe_rs(edge0: f64, edge1: f64, x: f64) -> f64 {
    if !(edge0.is_finite() && edge1.is_finite() && x.is_finite()) { return f64::NAN; }
    if edge0 == edge1 { return f64::NAN; }
    let mut t = (x - edge0) / (edge1 - edge0);
    if t < 0.0 { t = 0.0; }
    if t > 1.0 { t = 1.0; }
    t * t * (3.0 - 2.0 * t)
}
