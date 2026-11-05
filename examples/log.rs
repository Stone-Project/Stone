// stone:job stone:math.log
// stone:function log_rs

#[no_mangle]
pub extern "C" fn log_rs(x: f64) -> f64 {
    if x <= 0.0 { return f64::NAN; }
    x.ln()
}
