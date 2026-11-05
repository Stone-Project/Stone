// stone:job stone:math.bias
// stone:function bias_rs

#[no_mangle]
pub extern "C" fn bias_rs(x: f64, bias: f64) -> f64 {
    x.powf(bias.ln() / 0.5_f64.ln())
}
