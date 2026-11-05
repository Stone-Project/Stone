// stone:job stone:math.damp_safe
// stone:function damp_safe_rs

#[no_mangle]
pub extern "C" fn damp_safe_rs(current: f64, target: f64, rate: f64, dt: f64) -> f64 {
    if !(current.is_finite() && target.is_finite() && rate.is_finite() && dt.is_finite()) { return f64::NAN; }
    if dt <= 0.0 { return f64::NAN; }
    current + (target - current) * (1.0 - (-rate * dt).exp())
}
