// stone:job stone:math.exp_decay
// stone:function exp_decay_rs

#[no_mangle]
pub extern "C" fn exp_decay_rs(value: f64, rate: f64, t: f64) -> f64 {
    value * (-rate * t).exp()
}
