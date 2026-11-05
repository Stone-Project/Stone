// stone:job stone:math.exp_decay_safe
// stone:function exp_decay_safe_rs

#[no_mangle]
pub extern "C" fn exp_decay_safe_rs(value: f64, rate: f64, t: f64) -> f64 {
    if !(value.is_finite() && rate.is_finite() && t.is_finite()) { return f64::NAN; }
    if t < 0.0 { return f64::NAN; }
    value * (-rate * t).exp()
}
