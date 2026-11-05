// stone:job stone:math.bias_safe
// stone:function bias_safe_rs

#[no_mangle]
pub extern "C" fn bias_safe_rs(x: f64, bias: f64) -> f64 {
    if !(x.is_finite() && bias.is_finite()) { return f64::NAN; }
    x.powf(bias.ln() / 0.5_f64.ln())
}
