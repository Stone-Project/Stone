// stone:job stone:math.mix_safe
// stone:function mix_safe_rs

#[no_mangle]
pub extern "C" fn mix_safe_rs(a: f64, b: f64, t: f64) -> f64 {
    if !(a.is_finite() && b.is_finite() && t.is_finite()) { return f64::NAN; }
    a + (b - a) * t
}
