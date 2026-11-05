// stone:job stone:math.ceil
// stone:function ceil_rs

#[no_mangle]
pub extern "C" fn ceil_rs(x: f64) -> f64 {
    x.ceil()
}
