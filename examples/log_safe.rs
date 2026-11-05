// stone:job stone:math.log_safe
// stone:function log_safe_rs

#[no_mangle]
pub extern "C" fn log_safe_rs(x: f64) -> f64 {
    if !x.is_finite() || x <= 0.0 { return f64::NAN; }
    x.ln()
}
