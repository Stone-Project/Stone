// stone:job stone:math.exp10_safe
// stone:function exp10_safe_rs

#[no_mangle]
pub extern "C" fn exp10_safe_rs(x: f64) -> f64 {
    if !x.is_finite() { return f64::NAN; }
    let r = 10.0_f64.powf(x);
    if r.is_finite() { r } else { f64::NAN }
}
