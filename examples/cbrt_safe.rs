// stone:job stone:math.cbrt_safe
// stone:function cbrt_safe_rs

#[no_mangle]
pub extern "C" fn cbrt_safe_rs(x: f64) -> f64 {
    if !x.is_finite() { return f64::NAN; }
    x.abs().powf(1.0 / 3.0).copysign(x)
}
