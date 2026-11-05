// stone:job stone:math.quantize
// stone:function quantize_rs

#[no_mangle]
pub extern "C" fn quantize_rs(x: f64, step: f64) -> f64 { (x / step).floor() * step }
