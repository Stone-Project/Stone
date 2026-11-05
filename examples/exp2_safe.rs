// stone:job stone:math.exp2_safe
// stone:function exp2_safe_rs

#[no_mangle]
pub extern "C" fn exp2_safe_rs(x: f64) -> f64 {
    if !x.is_finite() { return f64::NAN; }
    let r = 2.0_f64.powf(x);
    if r.is_finite() { r } else { f64::NAN }
}
