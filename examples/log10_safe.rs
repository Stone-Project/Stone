// stone:job stone:math.log10_safe
// stone:function log10_safe_rs

#[no_mangle]
pub extern "C" fn log10_safe_rs(x: f64) -> f64 {
    if !x.is_finite() || x <= 0.0 { return f64::NAN; }
    x.log10()
}
