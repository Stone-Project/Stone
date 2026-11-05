// stone:job stone:math.log2
// stone:function log2_rs

#[no_mangle]
pub extern "C" fn log2_rs(x: f64) -> f64 {
    if x <= 0.0 { return f64::NAN; }
    x.log2()
}
